

def get_tree_dict():
    tree = {
        "sha": "9fb037999f264ba9a7fc6274d15fa3ae2ab98312",
        "url": "https://api.github.com/repos/octocat/Hello-World/trees/9fb037999f264ba9a7fc6274d15fa3ae2ab98312",
        "tree": [
            {
                "path": "geolinkeddata.owl",
                "mode": "100644",
                "type": "blob",
                "size": 30,
                "sha": "44b4fc6d56897b048c772eb4087f854f46256132",
                "url": "https://api.github.com/repos/octocat/Hello-World/git/blobs/44b4fc6d56897b048c772eb4087f854f46256132"
            },
            {
                "path": "subdir",
                "mode": "040000",
                "type": "tree",
                "sha": "f484d249c660418515fb01c2b9662073663c242e",
                "url": "https://api.github.com/repos/octocat/Hello-World/git/blobs/f484d249c660418515fb01c2b9662073663c242e"
            },
            {
                "path": "alo.owl",
                "mode": "100755",
                "type": "blob",
                "size": 75,
                "sha": "45b983be36b73c0788dc9cbcb76cbb80fc7bb057",
                "url": "https://api.github.com/repos/octocat/Hello-World/git/blobs/45b983be36b73c0788dc9cbcb76cbb80fc7bb057"
            }
        ],
        "truncated": False
    }
    return tree