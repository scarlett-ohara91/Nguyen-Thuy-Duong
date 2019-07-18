from youtube_dl import YoutubeDL

options = {

    'default_search': 'ytsearch', # tell downloader to search instead of directly downloading

    'max_downloads': 1, # Tell downloader to download only the first entry (audio)

    'format': 'bestaudio/audio'

}

dl = YoutubeDL(options)

dl.download(['Nhớ mưa sài gòn lam trường'])

 