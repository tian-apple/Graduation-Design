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
        uint256 time; //时间戳
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
        commiditys.push(
            Commidity(name, priceandnumber, controlists, block.timestamp) //同时将交易时间戳写入区块链
        );
    }

    function getdata(
        string memory id //根据用户id获取商品信息
    )
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

    function getrandomdata(
        uint256 i //随机获取商品信息
    )
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
        //获取商品数量
        return commiditys.length;
    }

    function cleanup() public {
        //清空商品信息
        delete commiditys;
    }

    function getall() public view returns (Commidity[] memory) {
        //获取所有商品信息，返回的是结构体数组，每个元素格式为{加密商品名称，加密商品价格及数量，访问控制列表{授权的用户id，密钥序列}，时间戳}
        return commiditys;
    }
}
