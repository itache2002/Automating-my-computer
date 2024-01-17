import os
import shutil


sorce ='C://Users//Asus//Downloads'
img_dir='d://image'
zip_dir='d://Zip_folders'
doc_dir='d://doc'
rar_dir='d://rar'
pdf_dir='d://ppt_pdf'


obj=os.scandir(sorce)
# looping through downlode folder
for i in obj:
    if i.is_dir or i.is_file:

        # sorting jpg,jpeg,png imager in downlode folder and moving it to img_dir folder
        if i.name.endswith('JPG')or i.name.endswith('JPEG') or i.name.endswith('PNG')or i.name.endswith('jpg')or i.name.endswith('jpeg') or i.name.endswith('png'):
            sorce_file=os.path.join(sorce,i.name)
            img_file=os.path.join(img_dir,i.name)
            print(sorce_file)
            print(img_file)
            print("__________________________________________________")
            if not os.path.exists(img_file):
                shutil.move(sorce_file,img_file)

        # Sorting Zip files 
        if i.name.endswith('ZIP')or i.name.endswith('zip')  :
            sorce_file=os.path.join(sorce,i.name)
            zip_file=os.path.join(zip_dir,i.name)
            print(sorce_file)
            print(zip_file)
            print("__________________________________________________")
            if not os.path.exists(zip_file):
                shutil.move(sorce_file,zip_file)

        # Sorting Zip docx files 
        if  i.name.endswith('doc')or i.name.endswith('docx') :
            sorce_file=os.path.join(sorce,i.name)
            docx_file=os.path.join(doc_dir,i.name)
            print(sorce_file)
            print(docx_file)
            print("__________________________________________________")
            if not os.path.exists(docx_file):
                shutil.move(sorce_file,docx_file)

        # Sorting rar files        
        if i.name.endswith('rar')or i.name.endswith('RAR'):
            sorce_file=os.path.join(sorce,i.name)
            rar_file=os.path.join(rar_dir,i.name)
            print(sorce_file)
            print(rar_file)
            print("__________________________________________________")
            if not os.path.exists(rar_file):
                shutil.move(sorce_file,rar_file)
        #Sorting  PDF,PTT files
        if i.name.endswith('pptx')or i.name.endswith('pdf') or i.name.endswith('PPTX') :
            sorce_file=os.path.join(sorce,i.name)
            pdf_file=os.path.join(pdf_dir,i.name)
            print(sorce_file)
            print(pdf_file)
            print("__________________________________________________")
            if not os.path.exists(pdf_file):
                shutil.move(sorce_file,pdf_file)  

        
        
         

