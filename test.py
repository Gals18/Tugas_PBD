from minio import Minio
client = Minio(
    "localhost:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
    secure=False
)
data = client.get_object("galuhgrace","tweets.csv")

with open("file","wb") as file_data:
    for d in data:
        file_data.write(d)

