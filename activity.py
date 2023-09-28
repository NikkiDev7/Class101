import dropbox

class TransferData:
    def __init__(self, accessToken):
        self.accessToken = accessToken
    def uploadFiles(self, fileFrom, fileTo):
        db = dropbox.Dropbox(self.accessToken)
        file = open(fileFrom, "rb")
        db.files_upload(file.read(),fileTo)

def main():
    accessToken = "sl.Bm8h1ttl3tpDMsAWeuoYYThw0cnN6I2OQsONr_kstRJg3mMhq-bWw2VmGQKTo9akU4MPqOYfG81h2JJQ9EbIiDkVvQ3en4rITRKHmRJRQUSSevN8EcgdIgqbEVG5vYx6fgFx6U0XGsuS"
    transferData = TransferData(accessToken)
    file_from = 'test.txt'
    file_to = '/test_dropbox/test.txt'  # The full path to upload the file to, including the file name

    # API v2
    transferData.uploadFiles(file_from, file_to)


main()