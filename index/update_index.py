from pymongo import MongoClient, ASCENDING
from pymongo.operations import IndexModel

# Kết nối tới cơ sở dữ liệu MongoDB
client = MongoClient("mongodb://xx.xx.xx.xx:27017/")
db = client["countly"]


def update_indexes_smart_ux():
    # Tìm và đánh index tăng dần cho các cột trong các bảng có tên chứa "click_events"
    index = "screen_size_type_1_events.segmentation.domain_1_events.segmentation.view_1_events.segmentation.type_1_timestamp_1"
    for collection_name in db.list_collection_names(filter={"name": {"$regex": "click_events"}}):
        collection = db[collection_name]
        index_info = collection.index_information()
        # print(index_info)
        if index not in index_info.keys():
            print(collection)
            collection.create_index([
                ("screen_size_type", ASCENDING),
                ("events.segmentation.domain", ASCENDING),
                ("events.segmentation.view", ASCENDING),
                ("events.segmentation.type", ASCENDING),
                ("timestamp", ASCENDING)
            ])


if __name__ == "__main__":
    update_indexes_smart_ux()