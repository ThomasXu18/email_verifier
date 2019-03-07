from dns import resolver
from smtplib import SMTP, SMTPServerDisconnected
import pprint


def find_mx_record(*, host):
    """找到指定邮件后缀的 MX 记录
    """
    try:
        mx_records = [record.to_text().split() for record in resolver.query(host, 'MX')]
    except (resolver.NoAnswer, resolver.NXDOMAIN, resolver.NoNameservers):
        mx_records = []
    return mx_records


def verify(email, smtp_host):
    """校验email的地址是否真实存在
    """
    try:
        with SMTP(smtp_host) as smtp:
            # send the HELO command
            smtp.helo()
            # send the MAIL FROM
            smtp.mail('test@hotmail.com') 
            # send the RCPT TO
            resp = smtp.rcpt(email)
            # check the status code
            return resp[0] == 250 or resp[0] == 251
    except SMTPServerDisconnected:
        return False

if __name__ == "__main__":
    pprint.pprint(find_mx_record(host='gmail.com'))

    pprint.pprint(verify("cmsdnfnskdnfkds@gmail.com", 'alt2.gmail-smtp-in.l.google.com'))
    pprint.pprint(verify("xupengfei806@gmail.com", 'alt2.gmail-smtp-in.l.google.com'))
