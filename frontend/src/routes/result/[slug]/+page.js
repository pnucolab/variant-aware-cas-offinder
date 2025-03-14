
/** @type {import('./$types').PageLoad} */
export async function load({ params }) {
    return { ticket: params.slug };
  }