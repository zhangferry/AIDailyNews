<script lang="ts">
  import { onMount } from "svelte";
  import SearchIcon from "./SearchIcon.svelte";
  import PostSearchPreview from "./PostSearchPreview.svelte";

  let searchInput;
  let searchableDocs;
  let searchIndex;

  let searchQuery = "";
  let searchResults = [];
  let isSearching = false;

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
    if (searchQuery && searchQuery.length >= 2) {
      isSearching = true;
      const matches = searchIndex.search(searchQuery);
      searchResults = [];
      matches.map((match) => {
        searchableDocs.filter((doc) => {
          if (match.ref === doc.slug) {
            searchResults.push(doc);
          }
        });
      });
      isSearching = false;
    } else {
      searchResults = [];
    }
  }
</script>

<div class="search-container">
  <div class="search-wrapper">
    <!-- Search header with icon -->
    <div class="search-header">
      <div class="search-icon-wrapper">
        <SearchIcon found={searchResults.length > 0} />
      </div>
      <div class="search-input-wrapper">
        <input
          type="text"
          name="search"
          bind:this={searchInput}
          placeholder="搜索文章、标签..."
          bind:value={searchQuery}
          class="search-input"
        />
        {#if searchQuery}
          <button
            class="clear-btn"
            on:click={() => searchQuery = ''}
            aria-label="清除搜索"
          >
            ✕
          </button>
        {/if}
      </div>
    </div>

    <!-- Search status -->
    {#if searchQuery.length >= 2}
      <div class="search-status">
        {#if isSearching}
          <span class="status-text searching">搜索中...</span>
        {:else if searchResults.length > 0}
          <span class="status-text">找到 {searchResults.length} 篇文章</span>
        {:else}
          <span class="status-text no-results">未找到相关文章</span>
        {/if}
      </div>
    {/if}

    <!-- Search results -->
    <div class="search__results" class:has-results={searchResults.length > 0}>
      {#if searchResults.length}
        <div class="results-list">
          {#each searchResults as post, i}
            <div class="result-item" style="animation-delay: {i * 50}ms">
              <PostSearchPreview {post} isLast={i === searchResults.length - 1} />
            </div>
          {/each}
        </div>
      {:else if searchQuery.length >= 2}
        <div class="empty-state">
          <div class="empty-icon">🔍</div>
          <p class="empty-text">未找到匹配的文章</p>
          <p class="empty-hint">尝试使用其他关键词搜索</p>
        </div>
      {:else}
        <div class="initial-state">
          <div class="initial-icon">💡</div>
          <p class="initial-text">输入关键词搜索文章</p>
          <div class="search-tips">
            <span class="tip-tag">标题</span>
            <span class="tip-tag">描述</span>
            <span class="tip-tag">标签</span>
          </div>
        </div>
      {/if}
    </div>

    <!-- Footer note -->
    <div class="search-footer">
      <span class="keyboard-hint">
        <kbd>ESC</kbd> 关闭
      </span>
    </div>
  </div>
</div>

<style>
  .search-container {
    @apply w-full max-w-3xl mx-auto;
  }

  .search-wrapper {
    @apply relative bg-theme-primary rounded-2xl shadow-2xl overflow-hidden;
    background: linear-gradient(135deg,
      rgba(255, 255, 255, 0.95) 0%,
      rgba(248, 250, 252, 0.98) 100%
    );
    border: 1px solid rgba(91, 124, 153, 0.15);
    box-shadow:
      0 25px 50px -12px rgba(91, 124, 153, 0.25),
      0 0 0 1px rgba(255, 255, 255, 0.5) inset;
    transition: all 0.3s ease-out;
  }

  :global(html.dark) .search-wrapper {
    background: linear-gradient(135deg,
      rgba(26, 26, 46, 0.98) 0%,
      rgba(30, 30, 50, 0.95) 100%
    );
    border: 1px solid rgba(107, 184, 184, 0.2);
    box-shadow:
      0 25px 50px -12px rgba(0, 0, 0, 0.5),
      0 0 0 1px rgba(107, 184, 184, 0.1) inset,
      0 0 40px rgba(107, 184, 184, 0.1);
  }

  .search-wrapper:focus-within {
    transform: translateY(-2px);
    box-shadow:
      0 30px 60px -12px rgba(91, 124, 153, 0.3),
      0 0 0 1px rgba(91, 124, 153, 0.2) inset;
  }

  :global(html.dark) .search-wrapper:focus-within {
    box-shadow:
      0 30px 60px -12px rgba(0, 0, 0, 0.6),
      0 0 0 1px rgba(107, 184, 184, 0.2) inset,
      0 0 50px rgba(107, 184, 184, 0.15);
  }

  /* Search header */
  .search-header {
    @apply relative p-6 pb-4;
    border-bottom: 1px solid rgba(91, 124, 153, 0.1);
  }

  :global(html.dark) .search-header {
    border-bottom: 1px solid rgba(107, 184, 184, 0.1);
  }

  .search-icon-wrapper {
    @apply absolute left-6 top-1/2 -translate-y-1/2;
    @apply text-theme-primary;
    transition: all 0.3s ease-out;
  }

  :global(html.dark) .search-icon-wrapper {
    @apply text-theme-dark-primary;
  }

  .search-wrapper:focus-within .search-icon-wrapper {
    transform: translateY(-50%) scale(1.1);
  }

  .search-input-wrapper {
    @apply relative pl-12 pr-10;
  }

  .search-input {
    @apply w-full px-0 py-3 text-xl font-display font-medium;
    @apply text-theme-text-primary bg-transparent border-0;
    @apply placeholder-theme-text-secondary;
    @apply focus:outline-none focus:ring-0;
    transition: all 0.3s ease-out;
  }

  :global(html.dark) .search-input {
    @apply text-theme-dark-text-primary placeholder-theme-dark-text-secondary;
  }

  .search-input::placeholder {
    opacity: 0.5;
    transition: opacity 0.3s ease-out;
  }

  .search-input:focus::placeholder {
    opacity: 0.3;
  }

  .clear-btn {
    @apply absolute right-0 top-1/2 -translate-y-1/2;
    @apply w-6 h-6 flex items-center justify-center;
    @apply text-theme-text-secondary;
    @apply rounded-full bg-theme-surface/80;
    @apply transition-all duration-200;
    @apply hover:bg-theme-primary hover:text-theme-primary;
    @apply hover:scale-110;
    font-size: 14px;
    line-height: 1;
  }

  :global(html.dark) .clear-btn {
    @apply text-theme-dark-text-secondary bg-theme-dark-surface/80;
    @apply hover:bg-theme-dark-primary hover:text-theme-dark-primary;
  }

  /* Search status */
  .search-status {
    @apply px-6 py-3 text-sm;
    background: linear-gradient(90deg,
      rgba(91, 124, 153, 0.03) 0%,
      rgba(107, 184, 184, 0.05) 100%
    );
    border-bottom: 1px solid rgba(91, 124, 153, 0.08);
  }

  :global(html.dark) .search-status {
    background: linear-gradient(90deg,
      rgba(107, 184, 184, 0.05) 0%,
      rgba(212, 165, 165, 0.03) 100%
    );
    border-bottom: 1px solid rgba(107, 184, 184, 0.1);
  }

  .status-text {
    @apply text-theme-text-secondary font-medium;
  }

  :global(html.dark) .status-text {
    @apply text-theme-dark-text-secondary;
  }

  .status-text.searching {
    @apply text-theme-primary;
  }

  :global(html.dark) .status-text.searching {
    @apply text-theme-dark-primary;
  }

  .status-text.no-results {
    @apply text-theme-text-muted;
  }

  :global(html.dark) .status-text.no-results {
    @apply text-theme-dark-text-muted;
  }

  /* Results container */
  .search__results {
    @apply w-full overflow-y-auto;
    max-height: 60vh;
    min-height: 200px;
    padding: 0;
  }

  .search__results.has-results {
    @apply px-4 py-4;
  }

  .results-list {
    @apply space-y-2;
  }

  .result-item {
    animation: slideIn 0.3s ease-out forwards;
    opacity: 0;
  }

  @keyframes slideIn {
    from {
      opacity: 0;
      transform: translateX(-10px);
    }
    to {
      opacity: 1;
      transform: translateX(0);
    }
  }

  /* Empty state */
  .empty-state,
  .initial-state {
    @apply flex flex-col items-center justify-center;
    @apply py-16 px-6 text-center;
  }

  .empty-icon,
  .initial-icon {
    @apply text-5xl mb-4;
    opacity: 0.6;
  }

  .empty-text,
  .initial-text {
    @apply text-lg font-medium text-theme-text-primary mb-2;
  }

  :global(html.dark) .empty-text,
  :global(html.dark) .initial-text {
    @apply text-theme-dark-text-primary;
  }

  .empty-hint {
    @apply text-sm text-theme-text-muted;
  }

  :global(html.dark) .empty-hint {
    @apply text-theme-dark-text-muted;
  }

  .search-tips {
    @apply flex flex-wrap gap-2 justify-center mt-4;
  }

  .tip-tag {
    @apply px-3 py-1 text-xs font-medium rounded-full;
    @apply bg-theme-primary/10 text-theme-primary border border-theme-primary/20;
  }

  :global(html.dark) .tip-tag {
    @apply bg-theme-dark-primary/20 text-theme-dark-primary border-theme-dark-primary/30;
  }

  /* Footer */
  .search-footer {
    @apply px-6 py-4 border-t border-theme-border/20;
    @apply flex justify-center;
  }

  :global(html.dark) .search-footer {
    @apply border-t border-theme-dark-border/30;
  }

  .keyboard-hint {
    @apply text-xs text-theme-text-muted;
    @apply flex items-center gap-2;
  }

  :global(html.dark) .keyboard-hint {
    @apply text-theme-dark-text-muted;
  }

  .keyboard-hint kbd {
    @apply px-2 py-1 rounded;
    @apply bg-theme-surface border border-theme-border/50;
    @apply font-mono text-xs;
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
  }

  :global(html.dark) .keyboard-hint kbd {
    @apply bg-theme-dark-surface border-theme-dark-border/50;
  }

  /* Scrollbar styling for results */
  .search__results::-webkit-scrollbar {
    @apply w-2;
  }

  .search__results::-webkit-scrollbar-track {
    @apply bg-transparent;
  }

  .search__results::-webkit-scrollbar-thumb {
    @apply bg-theme-primary/30 rounded-full;
  }

  :global(html.dark) .search__results::-webkit-scrollbar-thumb {
    @apply bg-theme-dark-primary/30;
  }

  .search__results::-webkit-scrollbar-thumb:hover {
    @apply bg-theme-primary/50;
  }

  :global(html.dark) .search__results::-webkit-scrollbar-thumb:hover {
    @apply bg-theme-dark-primary/50;
  }
</style>
