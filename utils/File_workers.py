
class file_workers:
    def add_url(url, file_path):
        full_path=f"/home/np_1961/parser/{file_path}"
        followers_txt_file=open(full_path,'a')
        followers_txt_file.write(url+'\n')
        followers_txt_file.close()

    
    def txt_file_update(file_path):
        
        full_path=f"/home/np_1961/parser/{file_path}"   

        txt_file=open(full_path).readlines()       
        txt_file=[line.split('\n')[0] for line in txt_file]
        txt_file=[line for line in txt_file if line]
        txt_file=list(set(txt_file))
        
        file_workers.txt_file_init_(file_path=file_path)
        for url in txt_file:
            file_workers.add_url(url=url, file_path=file_path)
        return txt_file
    
    def txt_file_init_(file_path):
        full_path=f"/home/np_1961/parser/{file_path}"   
        file=open(full_path, 'w')
        file.close()
    
    def del_url(url,file_path):
        lines=file_workers.txt_file_update(file_path=file_path)
        lines=[line for line in lines if line !=url]

        file_workers.txt_file_init_(file_path=file_path)
        [file_workers.add_url(url=line,
                                file_path=file_path) for line in lines]
        
