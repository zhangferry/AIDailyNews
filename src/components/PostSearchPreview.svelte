<script lang="ts">
    type Props = {
        slug: string
        title: string
        description: string
        category: string,
        tags: Array<string>
    }
    export let post: Props
    export let isLast: boolean = false
</script>
<div class="post-preview">
    <div class="post-content">
        <h4 class="post-preview__title">
            <a href={`/${post.category}/${post.slug}`} title={post.title}>
                {post.title}
                <span class="arrow">→</span>
            </a>
        </h4>
        <p class="post-preview__desc">
            {post.description}
        </p>
        <ul class="tag-list">
            {#each post.tags as tag}
                <a class="tag" href={`/tags/${tag}`} title={tag}>{tag}</a>
            {/each}
        </ul>
    </div>
</div>
<style lang="postcss">
    .post-preview {
        @apply relative;
        @apply p-4 rounded-xl;
        @apply transition-all duration-200 ease-out;
        @apply hover:bg-theme-surface/50;
    }

    :global(html.dark) .post-preview {
        @apply hover:bg-theme-dark-surface/50;
    }

    .post-preview:hover {
        transform: translateX(4px);
        background: linear-gradient(90deg,
          rgba(91, 124, 153, 0.05) 0%,
          rgba(107, 184, 184, 0.03) 100%
        );
    }

    :global(html.dark) .post-preview:hover {
        background: linear-gradient(90deg,
          rgba(107, 184, 184, 0.08) 0%,
          rgba(212, 165, 165, 0.03) 100%
        );
    }

    .post-content {
        @apply flex flex-col gap-3;
    }

    .post-preview__title {
        @apply text-base leading-tight font-semibold text-theme-text-primary;
    }

    :global(html.dark) .post-preview__title {
        @apply text-theme-dark-text-primary;
    }

    .post-preview__title a {
        @apply flex items-center justify-between;
        @apply transition-all duration-200;
        text-decoration: none;
    }

    .post-preview__title a:hover {
        background: linear-gradient(90deg, #5b7c99 0%, #6bb8b8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    :global(html.dark) .post-preview__title a:hover {
        background: linear-gradient(90deg, #6bb8b8 0%, #d4a5a5 100%);
        -webkit-background-clip: text;
        background-clip: text;
    }

    .arrow {
        @apply opacity-0 -translate-x-2;
        @apply transition-all duration-200 ease-out;
    }

    .post-preview:hover .arrow {
        @apply opacity-100 translate-x-0;
    }

    .post-preview__desc {
        @apply text-sm text-theme-text-secondary leading-relaxed line-clamp-2;
    }

    :global(html.dark) .post-preview__desc {
        @apply text-theme-dark-text-secondary;
    }

    .tag-list {
        @apply list-none flex flex-wrap gap-2;
    }

    .tag {
        @apply inline-block text-xs px-3 py-1 rounded-full font-medium;
        @apply text-theme-primary bg-theme-primary/10 border border-theme-primary/20;
        @apply transition-all duration-200;
        @apply hover:bg-theme-primary/20 hover:border-theme-primary/30 hover:scale-105;
        text-decoration: none;
    }

    :global(html.dark) .tag {
        @apply text-theme-dark-primary bg-theme-dark-primary/20 border-theme-dark-primary/30;
        @apply hover:bg-theme-dark-primary/30 hover:border-theme-dark-primary/40;
    }
</style>
