import hashlib


def md5(message, direction=1):
	return None if direction != 1 else hashlib.md5(str(message).encode('utf-8')).hexdigest()


def sha_1(message, direction=1):
	return None if direction != 1 else hashlib.sha1(str(message).encode('utf-8')).hexdigest()


def sha_224(message, direction=1):
	return None if direction != 1 else hashlib.sha224(str(message).encode('utf-8')).hexdigest()


def sha_224_3(message, direction=1):
	return None if direction != 1 else hashlib.sha3_224(str(message).encode('utf-8')).hexdigest()


def sha_256(message, direction=1):
	return None if direction != 1 else hashlib.sha256(message.encode('utf-8')).hexdigest()


def sha3_384(message, direction=1):
	return None if direction != 1 else hashlib.sha3_384(str(message).encode('utf-8')).hexdigest()


def sha_512(message, direction=1):
	return None if direction != 1 else hashlib.sha512(message.encode('utf-8')).hexdigest()


def sha3_512(message, direction=1):
	return None if direction != 1 else hashlib.sha3_512(message.encode('utf-8')).hexdigest()
