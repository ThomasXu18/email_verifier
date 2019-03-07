
import asyncio
import aiohttp

async def judge(email):
    url = r"""https://mail.google.com/mail/gxlu?email="""+email
    async with aiohttp.ClientSession() as client:
        async with client.get(url) as resp:
            if resp.headers.get('set-cookie', None) is not None:
                return email
    return None

def verify(emails: list)->list:
    """接受一个待验证的邮件列表
    
    @return 返回所有通过验证的邮件
    """
    loop = asyncio.get_event_loop()
    tasks = []
    for email in emails:
        tasks.append(judge(email))
    results = loop.run_until_complete(asyncio.gather(*tasks))
    loop.close()
    return results

if __name__ == "__main__":
    emails = [
        """替换成你需要验证的邮件列表"""
    ]
    print(verify(emails))

