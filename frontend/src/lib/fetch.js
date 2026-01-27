// @ts-ignore
import { PUBLIC_SITE_ROOT } from '$env/static/public';
let site_root = `${PUBLIC_SITE_ROOT}/api/v1/`;

export async function load(uri, method="GET", file=null) {

	let resp;
	if (method == "GET") {
		resp = await fetch(site_root + uri);
	} else if (method == "POST") {
		let data = null;
		if (file) {
			data = new FormData();
			data.append("file", file);
			console.log('[DEBUG fetch.js] FormData created, starting fetch to:', site_root + uri);
		}
		const fetchStart = performance.now();
		resp = await fetch(site_root + uri, {
			method: "POST",
			body: data,
		});
		const fetchEnd = performance.now();
		console.log('[DEBUG fetch.js] Fetch completed in', ((fetchEnd - fetchStart) / 1000).toFixed(2), 'seconds');
	}
	if (!resp.ok) {
		throw new Error(`HTTP error! status: ${resp.status}`);
	   }
	let rofftarget = await resp.json();
	return rofftarget;
}
