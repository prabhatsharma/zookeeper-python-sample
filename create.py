from kazoo.client import KazooClient

connection_string = "zookeeper-headless.zookeeper.svc.cluster.local:2181"

zk = KazooClient(hosts=connection_string)

zk.start()

zk.create("/aws/ec2/ebs/st1")

zk.stop()
