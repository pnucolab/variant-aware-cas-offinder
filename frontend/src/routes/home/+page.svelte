<script>
    import Top from '$lib/Top.svelte';
    import { Button } from 'flowbite-svelte';
</script>

<div class="cover-top w-full bg-cover bg-center flex flex-col items-center justify-center space-y-12 mb-8 -mx-[calc(50vw-50%)]" style="width: 100vw; height: 500px; margin-left: calc(50% - 50vw); background-image: url('/home-main.jpg');">
    <div class="text-center space-y-4">
        <h1 class="text-6xl font-bold mb-4 text-white">RGEN Toolkit</h1>
        <p class="mb-6 text-white">Provide powerful tools for RGEN research and analysis</p>
    </div>

    <div class="flex justify-center gap-4">
        <Button href="/about" color="dark" class="opacity-90 hover:opacity-100 text-white text-xl">About RGEN Toolkit</Button>
    </div>
</div>
