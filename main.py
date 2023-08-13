import speedtest
import matplotlib.pyplot as plt

print('''                          _                       _                 __   ___  
                         | |                     | |               /_ | / _ \ 
  ___ _ __   ___  ___  __| | __ _ _ __ __ _ _ __ | |__   ___ _ __   | || | | |
 / __| '_ \ / _ \/ _ \/ _` |/ _` | '__/ _` | '_ \| '_ \ / _ \ '__|  | || | | |
 \__ \ |_) |  __/  __/ (_| | (_| | | | (_| | |_) | | | |  __/ |     | || |_| |
 |___/ .__/ \___|\___|\__,_|\__, |_|  \__,_| .__/|_| |_|\___|_|     |_(_)___/ 
     | |                     __/ |         | |                                
     |_|                    |___/          |_|                                ''')

def test_internet_speed():
    st = speedtest.Speedtest()
    st.get_best_server()

    download_speed = st.download() / 10**6
    upload_speed = st.upload() / 10**6
    return download_speed, upload_speed

if __name__ == "__main__":
    download, upload = test_internet_speed()
    print(f"Download Speed: {download:.2f} Mbps")
    print(f"Upload Speed: {upload:.2f} Mbps")

labels = ['Download', 'Upload']
speeds = [download, upload]

plt.bar(labels, speeds, color=['blue', 'green'])
plt.ylabel('Speed (Mbps)')
plt.title('Internet Speed Test Results')
plt.show()