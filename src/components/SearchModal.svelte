<script lang="ts">
    import { fade, fly } from 'svelte/transition'
    import { elasticOut } from 'svelte/easing'
    import { onMount } from 'svelte'
    import { isSearchVisible } from '../store/search'
    import Search from './Search.svelte'

    const dismissModal = () => isSearchVisible.set(false)

    // Handle ESC key to close modal
    function handleKeydown(event: KeyboardEvent) {
        if (event.key === 'Escape') {
            dismissModal()
        }
    }

    let listenerAdded = false

    // Add/remove event listener when modal visibility changes
    $: if ($isSearchVisible && !listenerAdded && typeof window !== 'undefined') {
        window.addEventListener('keydown', handleKeydown)
        listenerAdded = true
    }

    $: if (!$isSearchVisible && listenerAdded && typeof window !== 'undefined') {
        window.removeEventListener('keydown', handleKeydown)
        listenerAdded = false
    }

</script>
{#if $isSearchVisible}
    <div class="modal__backdrop" role="button" tabindex="0" on:click={dismissModal} transition:fade={{ duration: 200 }}></div>
    <div class="modal" role="dialog">
        <div class="modal__cnt" transition:fly={{ y: -100, opacity: 1, duration: 500, easing: elasticOut }}>
            <Search />
        </div>
    </div>
{/if}
<style>
    .modal {
        @apply fixed top-0 left-0 w-full h-full grid justify-center content-start pt-[20vh] pointer-events-none z-50;
    }
    .modal__backdrop {
        @apply fixed top-0 left-0 w-full h-screen;
        background: linear-gradient(135deg,
            rgba(91, 124, 153, 0.15) 0%,
            rgba(107, 184, 184, 0.12) 50%,
            rgba(212, 165, 165, 0.15) 100%
        );
        backdrop-filter: blur(8px);
        z-index: 1;
        pointer-events: auto;
    }

    :global(html.dark) .modal__backdrop {
        background: linear-gradient(135deg,
            rgba(107, 184, 184, 0.2) 0%,
            rgba(212, 165, 165, 0.15) 50%,
            rgba(107, 184, 184, 0.2) 100%
        );
        backdrop-filter: blur(12px);
    }

    .modal__cnt {
        @apply w-full max-w-4xl px-4;
        z-index: 10;
        position: relative;
        pointer-events: none;
    }

    .modal__cnt :global(*) {
        pointer-events: auto;
    }
</style>
