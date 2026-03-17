<script lang="ts">
  import { onMount } from "svelte";
  import SearchIcon from "./SearchIcon.svelte";
  import PostSearchPreview from "./PostSearchPreview.svelte";

  let searchInput;
  let searchableDocs;
  let searchIndex;

  let searchQuery = "";
  let searchResults = [];

  onMount(async () => {
    const lunr = (await import("lunr")).default;
    const resp = await fetch("/search-index.json");
    searchableDocs = await resp.json();
    // Initialize indexing
    searchIndex = lunr(function () {
      // the match key...
      this.ref("slug");

      // indexable properties
      this.field("title");
      this.field("description");
      this.field("tags");

      // Omit, if you don't want to search on `body`
      // this.field('body')

      // Index every document
      searchableDocs.forEach((doc) => {
        this.add(doc);
      }, this);
    });
    searchInput.focus();
  });

  $: {
    if (searchQuery && searchQuery.length >= 3) {
      const matches = searchIndex.search(searchQuery);
      searchResults = [];
      matches.map((match) => {
        searchableDocs.filter((doc) => {
          if (match.ref === doc.slug) {
            searchResults.push(doc);
          }
        });
      });
    }
  }
</script>

<div class="search">
  <div class="search__ctrl">
    <label for="search"><SearchIcon found={searchResults.length > 0} /></label>
    <input
      type="text"
      name="search"
      bind:this={searchInput}
      placeholder="What are you looking for?"
      bind:value={searchQuery}
    />
  </div>
  <div class="search__results">
    {#if searchResults.length}
      {#each searchResults as post, i}
        <PostSearchPreview {post} isLast={i === searchResults.length - 1} />
      {/each}
    {:else}
      <div class="search__results--none">
        {#if searchQuery.length}
          No matching items found!
        {:else}
          Search something and let me find it for you! :-)
        {/if}
      </div>
    {/if}
  </div>
  <div class="note"><small>click anywhere outside to close</small></div>
</div>

<style>
  .search {
    @apply w-full relative bg-theme-primary p-8 rounded-md shadow-lg;
  }
  :global(html.dark) .search {
    @apply bg-theme-dark-primary;
  }
  input {
    @apply w-full px-4 py-2 pl-10 text-xl font-semibold text-theme-text-primary border-0 shadow-inner rounded-md bg-theme-surface placeholder-theme-text-secondary;
  }
  :global(html.dark) input {
    @apply text-theme-dark-text-primary bg-theme-dark-surface placeholder-theme-dark-text-secondary;
  }
  .search__ctrl {
    @apply pb-4 relative;
  }
  .search__ctrl label {
    @apply text-theme-primary absolute top-2 left-2;
  }
  :global(html.dark) .search__ctrl label {
    @apply text-theme-dark-primary;
  }
  .search__results {
    @apply w-96 h-64 py-4 overflow-y-auto;
  }
  .search__results--none {
    @apply text-center text-theme-text-primary;
  }
  :global(html.dark) .search__results--none {
    @apply text-theme-dark-text-primary;
  }
  .note {
    @apply w-full text-center text-theme-text-primary;
  }
  :global(html.dark) .note {
    @apply text-theme-dark-text-primary;
  }
</style>
