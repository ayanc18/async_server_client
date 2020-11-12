import asyncio
import aiohttp
import logging
import json
import random

api = 'http://0.0.0.0:8080/sendval/'
list_resp = []
max_threads = 10 #if not otherwise set

from bst import BST, Node


def __build_list(resp_obj):
    #list_resp.append(json.loads(resp.decode('utf-8')))
    list_resp.append(resp_obj)

async def get_body(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, timeout=30) as response:
            assert response.status == 200
            resp = await response.read()
            return resp

async def get_results(url):
    resp_obj = {}
    resp = await get_body(url)
    resp_obj = json.loads(resp.decode('utf-8'))
    resp_obj['client_id'] = url.split('/')[5]
    __build_list(resp_obj)
    return 'FINISHED'

async def handle_tasks(task_id, work_queue):
    while not work_queue.empty():
        current_url = await work_queue.get()
        t = random.getrandbits(2)
        await asyncio.sleep(t)
        try:
            task_status = await get_results(current_url)
        except Exception as e:
            logging.exception('Error for {}'.format(current_url),exc_info=True)

def event_driver(urls,max_threads):
    q = asyncio.Queue()
    [q.put_nowait(url) for url in urls]
    loop = asyncio.get_event_loop()
    tasks = [handle_tasks(task_id, q, ) for task_id in range(max_threads)]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    with open('bst_client.json', 'w') as fp:
        json.dump(list_resp, fp)


if __name__ == '__main__':
    urls = []
    num_clients = input("Input the number of clients to send request: ")
    N = int(num_clients)
    max_threads = int(num_clients)
    for i in range(1,N+1):
        intval = random.getrandbits(64)
        url = api + str(intval) + '/' + str(i)
        urls.append(url)
    event_driver(urls,max_threads)
    #dumping the list of dict [i.e. client id and value key value pairs] as json file.

    # now opening the file and building the BST and doing inorder traversal to validate
    bin_tree = BST()
    f = open('bst_client.json', "r")
    node_list = json.load(f)
    for node in node_list:
        bin_tree.insert(node['value_received'],node['client_id'])
    #bst inorder from the client tree
    print("Inorder")
    print(bin_tree.inorder_traversal())
    print("preorder")
    print(bin_tree.preorder_traversal())
    print("postorder")
    print(bin_tree.postorder_traversal())
    f.close()
    del bin_tree
    '''

    #opening the server pkl BST object to verify.
    with open('bst_server.pkl', 'rb') as fp:
        bin2_tree = pickle.load(fp)

    print(bin2_tree.inorder())
    '''
    
    

