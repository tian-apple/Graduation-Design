module.exports = {
  networks: {
    development: {
      host: "127.0.0.1",
      port: 8900,
      network_id: "5777"
    },
  },
  mocha: {},
  compilers: {
    solc: {
      version: "0.8.17",
      settings: {
        optimizer: {
          enabled: true,
          runs: 200
        }
      }
    }
  }
};
