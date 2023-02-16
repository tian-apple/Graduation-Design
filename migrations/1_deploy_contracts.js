//迁移脚本
var Working = artifacts.require("./Working.sol");
module.exports = function (deployer) {
    deployer.deploy(Working);
};
// Path: migrations\1_deploy_contracts.js