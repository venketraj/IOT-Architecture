# import time module, Observer, FileSystemEventHandler
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__


def blob_upload():
    
    #DefaultEndpointsProtocol=https;AccountName=saretailstoreaudit;AccountKey=Q1DcRmzGT88kSqMtwaqrqAVBwXpMFIs1LK2tDcLw6cgyPOTCEIFatJawJAREMwkhTASJFIlioaNmh7z4rteRZrtg==;EndpointSuffix=core.windows.net
    print("Azure Blob Storage v" + __version__ + " - Python quickstart sample")
    #Enter the Connection string here 
    connect_str = "DefaultEndpointsProtocol=https;AccountName=saretailstoreaudit;AccountKey=Q1DcRmzT88kSqMtw6qrqAVBwXpMFIs1LK2tDcLw6cgyPoTCElFatJawJAREMwkhTASJFlIioaNmh7z4rteZrtg==;EndpointSuffix=core.windows.net"

    # Create the BlobServiceClient object which will be used to create a container client
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)

    # Create a unique name for the container
    container_name = "saazureedgecontainer"

    # Create the container
    #container_client = blob_service_client.create_container(container_name)

    # Create a local directory to hold blob data
    local_path = "D:/Node_red/Data_logger/Log_folder"


    # Create a file in the local data directory to upload and download
    local_file_name = "high_temp.csv"
    upload_file_path = os.path.join(local_path, local_file_name)

    # Create a blob client using the local file name as the name for the blob
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)

    print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)

    # Upload the created file
    with open(upload_file_path, "rb") as data:
        blob_client.upload_blob(data,overwrite=True)

        
class OnMyWatch:
	# Set the directory on watch
	watchDirectory = "D:/Node_red/Data_logger/Log_folder"

	def __init__(self):
		self.observer = Observer()

	def run(self):
		event_handler = Handler()
		self.observer.schedule(event_handler, self.watchDirectory, recursive = True)
		self.observer.start()
		try:
			while True:
				time.sleep(5)
		except:
			self.observer.stop()
			print("Observer Stopped")

		self.observer.join()


class Handler(FileSystemEventHandler):

	@staticmethod
	def on_any_event(event):
		if event.is_directory:
			return None

		elif event.event_type == 'created':
			# Event is created, you can process it now
			print("Watchdog received created event - % s." % event.src_path)
		elif event.event_type == 'modified':
			# Event is modified, you can process it now
			print("Watchdog received modified event - % s." % event.src_path)
			blob_upload()
			



   


if __name__ == '__main__':
	watch = OnMyWatch()
	watch.run()
