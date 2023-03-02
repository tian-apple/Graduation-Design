pragma solidity >0.4.0 <0.9.0;

//数据混淆,智能合约包括一个数组[50]
//每次更新一个真实数据和4个假数据
contract Confuse {
    uint256[50] public confuse;

    constructor() public {
        for (uint256 i = 0; i < 50; i++) {
            confuse[i] = i;
        }
    }

    function update(uint256 i, uint256 value)
        public
        returns (
            uint256,
            uint256,
            uint256,
            uint256,
            uint256
        )
    {
        confuse[i] = value;
        //生成四个不一样的伪随机索引，改变数组中其他四个数据
        uint256 index1 = uint256(
            keccak256(abi.encodePacked(block.timestamp, block.difficulty, i))
        ) % 50;
        uint256 index2 = uint256(keccak256(abi.encodePacked(index1))) % 50;
        uint256 index3 = uint256(keccak256(abi.encodePacked(index2))) % 50;
        uint256 index4 = uint256(keccak256(abi.encodePacked(index3))) % 50;
        confuse[index1] =
            uint256(
                keccak256(
                    abi.encodePacked(block.timestamp, block.difficulty, i)
                )
            ) %
            50;
        confuse[index2] =
            uint256(
                keccak256(
                    abi.encodePacked(block.timestamp, block.difficulty, i)
                )
            ) %
            50;
        confuse[index3] =
            uint256(
                keccak256(
                    abi.encodePacked(block.timestamp, block.difficulty, i)
                )
            ) %
            50;
        confuse[index4] =
            uint256(
                keccak256(
                    abi.encodePacked(block.timestamp, block.difficulty, i)
                )
            ) %
            50;
        return (i, index1, index2, index3, index4);
    }

    function get(uint256 i) public view returns (uint256) {
        return confuse[i];
    }
}
