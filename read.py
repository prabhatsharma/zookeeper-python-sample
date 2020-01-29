from kazoo.client import KazooClient

connection_string = "zookeeper-headless.zookeeper.svc.cluster.local:2181"

zk = KazooClient(hosts=connection_string)

zk.start()

def get_node(path="/"):
    if zk.exists(path):
        # data, stat = zk.get(path)
        children = zk.get_children(path)
        # print("There are %s children with names %s" % (len(children), children))
        if len(children)>0:
            item = ""
            for child in children:
                if path[len(path)-1] == "/":
                    item = "/" + child
                    print(item)
                elif path[0] == "/":
                    item = path + "/" + child
                    print(item)
                else:
                    item = "/" + path + "/" + child
                    print(item)
                get_node(item)


get_node("/")
