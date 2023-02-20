pragma solidity >0.4.0 <0.9.0;

//存储数据结构体，包括加密字符字段，数值字段及访问控制列表
contract Working {
    struct Controlist {
        string userid; //用户id
        bytes keys; //密钥序列
    }
    struct Commidity {
        bytes commidity_name; //加密商品名称(明文为string类型)
        bytes commidity_priceandnumber; //加密商品价格及数量(明文为BFVvector类型)
        Controlist controlist; //访问控制列表
    }
    Commidity[] public commiditys; //存储商品信息
    Controlist public controlists; //存储访问控制列表

    function set(
        bytes memory name,
        bytes memory priceandnumber,
        string memory id,
        bytes memory kys
    ) public {
        controlists.userid = id;
        controlists.keys = kys;
        commiditys.push(Commidity(name, priceandnumber, controlists));
    }

    function getdata(string memory id)
        public
        view
        returns (
            bytes memory,
            bytes memory,
            string memory,
            bytes memory
        )
    {
        for (uint256 i = 0; i < commiditys.length; i++) {
            if (
                keccak256(abi.encode(commiditys[i].controlist.userid)) ==
                keccak256(abi.encode(id))
            )
                return (
                    commiditys[i].commidity_name,
                    commiditys[i].commidity_priceandnumber,
                    commiditys[i].controlist.userid,
                    commiditys[i].controlist.keys
                );
        }
    }

    function getrandomdata(uint256 i)
        public
        view
        returns (
            bytes memory,
            bytes memory,
            string memory,
            bytes memory
        )
    {
        return (
            commiditys[i].commidity_name,
            commiditys[i].commidity_priceandnumber,
            commiditys[i].controlist.userid,
            commiditys[i].controlist.keys
        );
    }

    function count() public view returns (uint256) {
        return commiditys.length;
    }

    function cleanup() public {
        delete commiditys;
    }
}
