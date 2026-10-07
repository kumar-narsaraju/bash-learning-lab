// Browser stand-in for node:zlib. gzip/zcat/rg -z are not available in the in-browser terminal.
const no = () => { throw new Error("gzip is not available in the browser terminal"); };
export const gunzipSync = no, gzipSync = no;
export const constants = { Z_BEST_COMPRESSION: 9, Z_BEST_SPEED: 1, Z_DEFAULT_COMPRESSION: -1 };
export default { gunzipSync, gzipSync, constants };
