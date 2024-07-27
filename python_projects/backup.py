# import os
# import shutil
# import datetime
# import schedule
# import time

# source_dir = "D:\sample_test_folder"
# destination_dir = "D:\sample_test_folder\Backups"

# def copy_folder_to_directory(source,dest):
#     today = datetime.date.today()
#     dest_dir = os.path.join(dest,str(today))
#     # print(f"dest_dir {dest_dir}")

#     try:
#         shutil.copytree(source,dest_dir)
#         print(f"Folder copied to {dest_dir}")
#     except FileExistsError:
#         print(f"Folder already exists in: {dest}")

# # def l():
# #     copy_folder_to_directory(source_dir,destination_dir)

# schedule.every().day.at("13:23").do(lambda: copy_folder_to_directory(source_dir,destination_dir))

# while True:
#     schedule.run_pending()
#     time.sleep(60)

        
