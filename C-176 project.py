from tkinter import*
import speedtest
import matplotlib.pyplot
import time

root=Tk()
root.title("internet speedtest project")
roo.geometry("500x500")

list_download_speed.append(download_speed)
list_upload_speed.append(upload_speed)

for i in range(5):
    
    def speedCheck():
        st=speedtest.Speedtest()
        download_speed = round(st.download()/1000000,2)
        label_downoad_speed['text']=str(download_speed) +"mbps"
        list_download_speed.append(download_speed)
        upload_speed = round(st.download()/1000000,2 )
        label_upload_speed['text']=str(upload_speed) +"mbps"
        list_upload_speed.append(upload_speed)
        time.sleep(no._of_seconds)
        No._of_seconds - 6
        print(list_download_speed)
        print(list_upload_speed)
        
list_x_axis.append(1,2,3,4,5)
list_y_axis.append(1.1,2.2,3.3,4.4,5.5)

plt.plot(x,list_download_speed, label="Download speed")
plt.plot(x,list_upload_speed,label="Upload speed")
plt.legend()
plt.show()



root.mailoop()


        
        
