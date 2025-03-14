
<script>
	import Bottom from '$lib/Bottom.svelte';
	import { Navbar, NavBrand, NavUl, NavLi, NavHamburger} from 'flowbite-svelte';
	import { page } from '$app/stores';
	import './styles.css';
</script>
<Navbar>
	<NavBrand href="/">
		<span class="text-xl font-bold ml-3 sm:ml-0">RGEN Toolkit</span>
	</NavBrand>
	<NavHamburger />
	<NavUl>
		<NavLi href="/" active={$page.url.pathname === '/'}>Variant-aware Cas-OFFinder</NavLi>
		<NavLi href="/about" active={$page.url.pathname === '/about'}>About</NavLi>
	</NavUl>
</Navbar>

<div class="px-4 sm:px-0">
	<div class="mx-auto flex mb-20 flex-col container">
		<slot />
	</div>
</div>

<Bottom />