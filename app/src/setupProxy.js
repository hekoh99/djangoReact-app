const { createProxyMiddleware } = require('http-proxy-middleware');

module.exports = function(app) {
  console.log('start');
  app.use("/api", createProxyMiddleware({
     target: "http://localhost:8000", changeOrigin: true, secure : false}));
};
