import qbittorrentapi
from qbittorrentapi import TorrentStates
import os
# import time

# settings
Host = '127.0.0.1'
Port = 8080
Username = 'hwucn'
Password = 'pass'
upload_limit = 8000000 # 这里单位为B，故对应8M/s

# instantiate a Client using the appropriate WebUI configuration
qbt_client = qbittorrentapi.Client(host=Host, port=Port, username=Username, password=Password)

# the Client will automatically acquire/maintain a logged in state in line with any request.
# therefore, this is not necessary; however, you may want to test the provided login credentials.
try:
    qbt_client.auth_log_in()
except qbittorrentapi.LoginFailed as e:
    print(e)

# display qBittorrent info
print(f'qBittorrent: {qbt_client.app.version}')
print(f'qBittorrent Web API: {qbt_client.app.web_api_version}')

if qbt_client.transfer_info()['up_info_speed'] > upload_limit:
    os.system("C:/amt.bat") # 改为自己的删种程序的路径
    exit(0)

# print(f"upload speed info: {qbt_client.transfer_info()['up_info_speed']}")
# for k,v in qbt_client.app.build_info.items(): print(f'{k}: {v}')
# print(f'qb webspeed: {qbt_client.get_torrent_webseeds()}')
# retrieve and show all torrents

# 检查是否有正在下载的种子
for torrent in qbt_client.torrents_info():
    print(f'{torrent.hash[-6:]}: {torrent.name} ({torrent.state}) {torrent.webseeds}')
    if torrent.state_enum.is_downloading:
        os.system("C:/amt.bat") # 改为自己的删种程序的路径
        exit(0)

# 没有正在下载的种子，加种
os.system("C:/flex.bat") # 该脚本会在加种之后进行磁盘空间检测


# pause all torrents
# qbt_client.torrents.pause.all()