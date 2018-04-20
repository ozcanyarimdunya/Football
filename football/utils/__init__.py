def convert_link(link=None, extra_url="/puan-durumu/"):
    if link is None:
        return "link is broken."

    link = link.split('/')
    return '/'.join(link[:-1]) + extra_url + link[-1]
