<script>
  import Bottom from '$lib/Bottom.svelte';
  import { Navbar, NavBrand, NavUl, NavLi, NavHamburger } from 'flowbite-svelte';
  import { page } from '$app/stores';
  import './styles.css';

  let hidden = true;
</script>

<Navbar
  class="fixed top-0 left-0 right-0 z-50 h-16 bg-white/95 dark:bg-gray-900/95 backdrop-blur-sm border-b border-gray-200 dark:border-gray-700 shadow-sm"
>
  <NavBrand href="/">
    <span class="text-xl font-bold ml-3 sm:ml-0 bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">
      RGE Toolkit
    </span>
  </NavBrand>

  <NavHamburger on:click={() => (hidden = !hidden)} />

  <NavUl {hidden}>
    <NavLi href="/var-cas-offinder" active={$page.url.pathname === '/var-cas-offinder'}>
      Variant-aware Cas-OFFinder
    </NavLi>
    <NavLi href="/about" active={$page.url.pathname === '/about'}>
      About
    </NavLi>
  </NavUl>
</Navbar>

<div class="pt-16 px-4 sm:px-0">
  <div class="mx-auto flex mb-20 flex-col container">
    <slot />
  </div>
</div>

<Bottom />
