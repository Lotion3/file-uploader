import dropbox

class TransferData:
    def __init__ (self,access_token):
        self.access_token=access_token

    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        with open(file_from,"rb") as f:
            dbx.files_upload(f.read(),file_to)

def main():
    access_token="sl.A2R9kxWSBlP9l0GJ38DSLAieUYwRs-fKUjp332-JrDa1zqXYQDP1V2mTwrKqiJLORSkuybvbCyQCwBdwhBxq0IuMnJkOnsrwNnutssqpKkDvLQqwlIXcT_hxa6Xktc39yn8qcTo"
    transferdata=TransferData(access_token)
    file_from="test.txt"
    file_to="/Alex Head/test.txt"
    transferdata.upload_file(file_from,file_to)

main()