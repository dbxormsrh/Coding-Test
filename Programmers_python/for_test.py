def perform_DB(x, a, b):
    query = 'where {a} < {x} < {b} order by {x} '.format(a, x, b)
    return list(query)   #DB에서 query 수행 후 결과값 받아옴.

def Verification_Request_from_Server(Start_CID, End_CID):       #검증을 하고자하는 영상의 첫 CID(Start_CID)와 마지막 CID(End_CID)
    #CID를 검증할 수 있는 public key list
    public_key_list = []

    #DB로부터 Start CID를 검증 가능한 public key를 가져온다.
    query = 'where {} < {} < {} order by desc key_ID limit 1'.format('key_ID', -1, Start_CID)
    public_key_list += (list(query))

    #DB로부터 Start CID부터 End CID를 검증 가능한 public key들을 가져온다.
    public_key_list += perform_DB('key_ID', Start_CID, End_CID)

    #CID에 대해 검증이 가능한 public key를 쌍으로 묶어놓은 dictionary
    key_to_CID = {}
    CID_list = []

    key_to_CID[public_key_list[0]] = perform_DB('CID', Start_CID, public_key_list[1])

    for i in range(1, len(public_key_list-1, 1)):
        key_to_CID[public_key_list[i]] = perform_DB('CID', public_key_list[i], public_key_list[i + 1])

    key_to_CID[public_key_list[0][-1]] = perform_DB('CID', public_key[-1], End_CID)
    
    #public key에 해당하는 CID list를 검증기에 보내 검증을 요청한다.
    for public_key, sub_CID_list in key_to_CID.items():
        Request_to_Verifier(public_key, sub_CID_list)