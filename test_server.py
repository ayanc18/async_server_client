from aiohttp import web
import json
import time
from multiprocessing import Process, Queue
import pickle
from bst import BST, Node

list_bst = []
bin_tree = BST()

async def handle_sendval(request):
    intval = request.match_info.get('intval')
    client_id = request.match_info.get('clientid')
    body = {
        'status': 'success',
        'value_received': intval
    }
    node = {
        'val' : intval,
        'id' : client_id
    }
    list_bst.append(node)
    bin_tree.insert(intval,client_id)    
    #q.put(list_bst)
    return web.Response(text=json.dumps(body))

def run_app():
    app = web.Application()
    app.router.add_route('GET', '/sendval/{intval}/{clientid}', handle_sendval)
    web.run_app(app)
    print(list_bst)
    with open('bst_server.pkl', 'wb') as fout:
        pickle.dump(bin_tree, fout, pickle.HIGHEST_PROTOCOL)


if __name__ == '__main__':
    run_app()
    '''
    p = Process(target=run_app, args=(q,))
    p.start()
    start = time.time()
    m = 10
    t = 0
    while t<=m:
        cur_time = time.time()
        t = cur_time - start
    list_bst_f = q.get()
    print(list_bst_f)
    '''
