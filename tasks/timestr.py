__all__ = (
    'seconds_to_str',
)


def seconds_to_str(seconds: int) -> str:
    days = int(seconds // (3600*24))
    seconds = seconds // (3600*24)
    hours = int(seconds // 3600)
    seconds = seconds // 3600
    mins = int(seconds // 60)
    sec = seconds
    ans = ''
    if(days != 0) :
        if(days < 10) : 
            ans = ans + '0' + str(days) + 'd'
        else :
            ans = ans + str(days) + 'd'
    #if(hours != 0) :
    raise NotImplementedError




