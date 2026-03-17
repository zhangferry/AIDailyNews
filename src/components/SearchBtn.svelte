<script lang="ts">
    import SearchIcon from './SearchIcon.svelte'
    import { isSearchVisible } from '../store/search'

    function showSearchDialog() {
        isSearchVisible.set(true)
    }
</script>

<button
    on:click={showSearchDialog}
    class="icon-button search-button"
    aria-label="Search"
>
    <SearchIcon />
</button>

<style>
  .search-button {
    @apply flex items-center justify-center;
    @apply w-9 h-9 md:w-10 md:h-10;
    @apply rounded-lg;
    @apply text-theme-text-muted;
    @apply bg-theme-surface border border-theme-border/50;
    @apply transition-all duration-200 ease-out;
    @apply hover:text-theme-primary hover:border-theme-primary hover:bg-theme-primary/10;
    @apply hover:scale-105 hover:-translate-y-0.5;
    @apply focus:outline-none focus:ring-2 focus:ring-theme-primary/50;
  }

  :global(html.dark) .search-button {
    @apply text-theme-dark-text-muted bg-theme-dark-surface border-theme-dark-border/50;
    @apply hover:text-theme-dark-primary hover:border-theme-dark-primary hover:bg-theme-dark-primary/10;
    @apply focus:ring-theme-dark-primary/50;
  }

  .search-button:hover {
    box-shadow: 0 4px 12px rgba(91, 124, 153, 0.15);
  }

  :global(html.dark) .search-button:hover {
    box-shadow: 0 4px 12px rgba(107, 184, 184, 0.15);
  }

  .search-button svg {
    @apply w-4 h-4 md:w-5 md:h-5;
  }
</style>
