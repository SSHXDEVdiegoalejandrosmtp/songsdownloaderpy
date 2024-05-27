# diegoalejadrochavez
# diegoalejadrochavez
# diegoalejadrochavez
# diegoalejadrochavez
# diegoalejadrochavez
# diegoalejadrochavez
# diegoalejadrochavez
# diegoalejadrochavez

import yt_dlp
from yt_dlp.utils import download_range_func
# diegoalejadrochavez

start_time = 2  # accepts decimal value like 2.3
end_time = 7  # the end 
# diegoalejadrochavez
# diegoalejadrochavez

yt_opts = {
    'verbose': True,
    'download_ranges': download_range_func(None, [(start_time, end_time)]),
    'force_keyframes_at_cuts': True, # Diegoalejadrochavez

}
# diegoalejadrochavez
with yt_dlp.YoutubeDL(yt_opts) as ydl:
    ydl.download("https://www.youtube.com/watch?v=BxU")
print(" developer diegoalejandro chavez cotactme  ")
# diegoalejadrochavez
