import asyncio
import json
from typing import Dict, Set, Union
from urllib import parse

import aiohttp


async def fetch(
    session: aiohttp.ClientSession, semaphore: asyncio.Semaphore, url: str
) -> dict:
    async with semaphore:
        async with session.get(
            url, allow_redirects=True, headers={"accept": "application/json"}
        ) as response:
            return await response.json()


def make_url(
    pkgname: str,
    repo_num: int = 1,
    distribution: str = "ubuntu",
    release: str = "20.04",
) -> str:
    query = parse.urlencode(
        {
            "all": "false",
            "pkgname": pkgname,
            "distribution": distribution,
            "release": release,
        }
    )
    return (
        f"https://packagemanager.rstudio.com/__api__/repos/{repo_num}/sysreqs?{query}"
    )


async def gather_requirements(max_requests: int = 4) -> Dict[str, dict]:
    with open("renv.lock", "rt") as infile:
        data = json.load(infile)

    pkgs = [val["Package"] for val in data["Packages"].values()]

    semaphore = asyncio.Semaphore(max_requests)

    async with aiohttp.ClientSession() as session:
        reqs = await asyncio.gather(
            *[fetch(session, semaphore, make_url(pkg)) for pkg in pkgs]
        )

    return {key: val for key, val in zip(pkgs, reqs)}


def _extract_apt_get(val: Union[list, str, dict]) -> Set[str]:
    if isinstance(val, list):
        output = set()
        for v in val:
            output |= _extract_apt_get(v)
        return output
    if isinstance(val, str):
        if val.startswith("apt-get install -y"):
            return {val[len("apt-get install -y ") :]}
    if isinstance(val, dict):
        return _extract_apt_get(list(val.values()))

    return set()


def convert_to_script(requirements: list) -> str:
    """
    Convert the requirements that are returned from RSPM into an apt-get line

    Args:
        requirements: The responses from RSPM

    Returns:
        apt-get install -y [requirements]
    """
    data = _extract_apt_get(requirements)
    return "apt-get install -y " + " ".join(sorted(data))


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    data = loop.run_until_complete(gather_requirements())
    print(convert_to_script(data))
