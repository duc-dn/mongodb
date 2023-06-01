import pymongo

client = pymongo.MongoClient("mongodb://10.159.28.52:31555/")

db = client["countly"]

col = db["heatmap_mobile_device_sizes"]

data = [
    {"device_model_name": "iPhone 14 Pro Max", "device_model_name_raw": "iPhone14ProMax", "size_inch": "6.7", "size_pixel": "2796 * 1290", "group": "iPhone 12/13/14 Pro Max", "screen_ratio": "19.5:9"},
    {"device_model_name": "iPhone 14 Plus", "device_model_name_raw": "iPhone14Plus", "size_inch": "6.7", "size_pixel": "2778 * 1284", "group": "iPhone 12/13/14 Pro Max", "screen_ratio": "19.5:9"},
    {"device_model_name": "iPhone 13 Pro Max", "device_model_name_raw": "iPhone13ProMax", "size_inch": "6.7", "size_pixel": "2778 * 1284", "group": "iPhone 12/13/14 Pro Max", "screen_ratio": "19.5:9"},
    {"device_model_name": "iPhone 12 Pro Max", "device_model_name_raw": "iPhone12ProMax", "size_inch": "6.7", "size_pixel": "2778 * 1284", "group": "iPhone 12/13/14 Pro Max", "screen_ratio": "19.5:9"},
    {"device_model_name": "iPhone 11 Pro Max", "device_model_name_raw": "iPhone11ProMax", "size_inch": "6.5", "size_pixel": "2688 * 1242", "group": "iPhone 11 Pro Max, iPhone XS Max", "screen_ratio": "19.5:9"},
    {"device_model_name": "iPhone XS Max", "device_model_name_raw": "iPhoneXSMax", "size_inch": "6.5", "size_pixel": "2688 * 1242", "group": "iPhone 11 Pro Max, iPhone XS Max", "screen_ratio": "19.5:9"},
    {"device_model_name": "iPhone 14 Pro", "device_model_name_raw": "iPhone14Pro","size_inch": "6.1", "size_pixel": "2556 * 1179", "group": "iPhone 12/13/14 Pro, iPhone 11/12/13/14/XR", "screen_ratio": "19.5:9"},
    {"device_model_name": "iPhone 14", "device_model_name_raw": "iPhone14", "size_inch": "6.1", "size_pixel": "2532 * 1170", "group": "iPhone 12/13/14 Pro, iPhone 11/12/13/14/XR", "screen_ratio": "19.5:9"},
    {"device_model_name": "iPhone 13 Pro", "device_model_name_raw": "iPhone13Pro", "size_inch": "6.1", "size_pixel": "2532 * 1170", "group": "iPhone 12/13/14 Pro, iPhone 11/12/13/14/XR", "screen_ratio": "19.5:9"},
    {"device_model_name": "iPhone 13", "device_model_name_raw": "iPhone13", "size_inch": "6.1", "size_pixel": "2532 * 1170", "group": "iPhone 12/13/14 Pro, iPhone 11/12/13/14/XR", "screen_ratio": "19.5:9"},
    {"device_model_name": "iPhone 12 Pro", "device_model_name_raw": "iPhone12Pro", "size_inch": "6.1", "size_pixel": "2532 * 1170", "group": "iPhone 12/13/14 Pro, iPhone 11/12/13/14/XR", "screen_ratio": "19.5:9"},
    {"device_model_name": "iPhone 12", "device_model_name_raw": "iPhone12", "size_inch": "6.1", "size_pixel": "2532 * 1170", "group": "iPhone 12/13/14 Pro, iPhone 11/12/13/14/XR", "screen_ratio": "19.5:9"},
    {"device_model_name": "iPhone 11", "device_model_name_raw": "iPhone11", "size_inch": "6.1", "size_pixel": "1792 * 828", "group": "iPhone 12/13/14 Pro, iPhone 11/12/13/14/XR", "screen_ratio": "19.5:9"},
    {"device_model_name": "iPhone XR", "device_model_name_raw": "iPhoneXR", "size_inch": "6.1", "size_pixel": "1792 * 828", "group": "iPhone 12/13/14 Pro, iPhone 11/12/13/14/XR", "screen_ratio": "19.5:9"},
    {"device_model_name": "iPhone 11 Pro", "device_model_name_raw": "iPhone11Pro", "size_inch": "5.8", "size_pixel": "2436 * 1125", "group": "iPhone X/XS/11 Pro", "screen_ratio": "19.5:9"},
    {"device_model_name": "iPhone XS", "device_model_name_raw": "iPhoneXS", "size_inch": "5.8", "size_pixel": "2436 * 1125", "group": "iPhone X/XS/11 Pro", "screen_ratio": "19.5:9"},
    {"device_model_name": "iPhone X", "device_model_name_raw": "iPhoneX", "size_inch": "5.8", "size_pixel": "2436 * 1125", "group": "iPhone X/XS/11 Pro", "screen_ratio": "19.5:9"},
    {"device_model_name": "iPhone 13 mini", "device_model_name_raw": "iPhone13mini", "size_inch": "5.4", "size_pixel": "2340 * 1080", "group": "iPhone 12/13 mini", "screen_ratio": "19.5:9"},
    {"device_model_name": "iPhone 12 mini", "device_model_name_raw": "iPhone12mini", "size_inch": "5.4", "size_pixel": "2340 * 1080", "group": "iPhone 12/13 mini", "screen_ratio": "19.5:9"},
    {"device_model_name": "iPhone 8 Plus", "device_model_name_raw": "iPhone8Plus", "size_inch": "5.5", "size_pixel": "1920 * 1080", "group": "iPhone 6/6S/7/8 Plus", "screen_ratio": "16:9"},
    {"device_model_name": "iPhone 7 Plus", "device_model_name_raw": "iPhone7Plus", "size_inch": "5.5", "size_pixel": "1920 * 1080", "group": "iPhone 6/6S/7/8 Plus", "screen_ratio": "16:9"},
    {"device_model_name": "iPhone 6S Plus", "device_model_name_raw": "iPhone6SPlus", "size_inch": "5.5", "size_pixel": "1920 * 1080", "group": "iPhone 6/6S/7/8 Plus", "screen_ratio": "16:9"},
    {"device_model_name": "iPhone 6 Plus", "device_model_name_raw": "iPhone6Plus", "size_inch": "5.5", "size_pixel": "1920 * 1080", "group": "iPhone 6/6S/7/8 Plus", "screen_ratio": "16:9"},
    {"device_model_name": "iPhone SE thế hệ thứ 3", "size_inch": "4.7", "size_pixel": "1344 * 750", "group": "iPhone 6/6S/7/8, iPhone SE(2)/SE(3)", "screen_ratio": "16:9"},
    {"device_model_name": "iPhone SE thế hệ thứ 2", "size_inch": "4.7", "size_pixel": "1344 * 750", "group": "iPhone 6/6S/7/8, iPhone SE(2)/SE(3)", "screen_ratio": "16:9"},
    {"device_model_name": "iPhone 8", "device_model_name_raw": "iPhone8", "size_inch": "4.7", "size_pixel": "1344 * 750", "group": "iPhone 6/6S/7/8, iPhone SE(2)/SE(3)", "screen_ratio": "16:9"},
    {"device_model_name": "iPhone 7", "device_model_name_raw": "iPhone7", "size_inch": "4.7", "size_pixel": "1344 * 750", "group": "iPhone 6/6S/7/8, iPhone SE(2)/SE(3)", "screen_ratio": "16:9"},
    {"device_model_name": "iPhone 6S", "device_model_name_raw": "iPhone6S", "size_inch": "4.7", "size_pixel": "1344 * 750", "group": "iPhone 6/6S/7/8, iPhone SE(2)/SE(3)", "screen_ratio": "16:9"},
    {"device_model_name": "iPhone 6", "device_model_name_raw": "iPhone6", "size_inch": "4.7", "size_pixel": "1344 * 750", "group": "iPhone 6/6S/7/8, iPhone SE(2)/SE(3)", "screen_ratio": "16:9"},
    {"device_model_name": "iPhone SE", "device_model_name_raw": "iPhoneSE", "size_inch": "4.0", "size_pixel": "1136 * 640", "group": "iPhone 5/5C/5S/SE(1)", "screen_ratio": "16:9"},
    {"device_model_name": "iPhone 5S", "device_model_name_raw": "iPhone5S", "size_inch": "4.0", "size_pixel": "1136 * 640", "group": "iPhone 5/5C/5S/SE(1)", "screen_ratio": "16:9"},
    {"device_model_name": "iPhone 5C", "device_model_name_raw": "iPhone5C", "size_inch": "4.0", "size_pixel": "1136 * 640", "group": "iPhone 5/5C/5S/SE(1)", "screen_ratio": "16:9"},
    {"device_model_name": "iPhone 5", "device_model_name_raw": "iPhone5", "size_inch": "4.0", "size_pixel": "1136 * 640", "group": "iPhone 5/5C/5S/SE(1)", "screen_ratio": "16:9"},
    {"device_model_name": "iPhone 4S", "device_model_name_raw": "iPhone4S", "size_inch": "3.5", "size_pixel": "960 * 640", "group": "iPhone 3G/3GS/4/4S", "screen_ratio": "3:2"},
    {"device_model_name": "iPhone 4", "device_model_name_raw": "iPhone4", "size_inch": "3.5", "size_pixel": "960 * 640", "group": "iPhone 3G/3GS/4/4S", "screen_ratio": "3:2"},
    {"device_model_name": "iPhone 3GS", "device_model_name_raw": "iPhone3GS", "size_inch": "3.5", "size_pixel": "480 * 320", "group": "iPhone 3G/3GS/4/4S", "screen_ratio": "3:2"},
    {"device_model_name": "iPhone 3G", "device_model_name_raw": "iPhone3G", "size_inch": "3.5", "size_pixel": "480 * 320", "group": "iPhone 3G/3GS/4/4S", "screen_ratio": "3:2"},
]

col.insert_many(data)