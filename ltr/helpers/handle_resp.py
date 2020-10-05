

def resp_msg(msg, resp, throw=True, verbose=False):
    if verbose:
        print('{} [Status: {}]'.format(msg, resp.status_code))
    if resp.status_code >= 400:
        if verbose:
            print(resp.text)
        if throw:
            raise RuntimeError(resp.text)

