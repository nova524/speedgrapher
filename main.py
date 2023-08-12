import speedtest
import matplotlib.pyplot as plt

def test_internet_speed():
    st = speedtest.Speedtest()
    st.get_best_server()

    download_speed = st.download() / 10**6  # Mbps로 변환
    upload_speed = st.upload() / 10**6  # Mbps로 변환

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