-- Добавляем Packer как пакет в Neovim
vim.cmd [[packadd packer.nvim]]

-- Используем данный коллбэк как список для плагинов
return require('packer').startup(function()

	-- Добавляем Packer в список, чтобы он обновлял сам себя
  use 'wbthomason/packer.nvim'
  -- Проводник
  use {'nvim-tree/nvim-tree.lua',
    requires = 'nvim-tree/nvim-web-devicons',
    tag = 'nightly'
  }
   -- интеграция с ranger  
  use 'kevinhwang91/rnvimr'
  -- Подсветка синтаксиса
  use {'nvim-treesitter/nvim-treesitter', run = ":TSUpdate"}
  -- Поиск
  -- use 'nvim-telescope/telescope-fzf-native.nvim'
 	use {'nvim-telescope/telescope.nvim', tag = '0.1.0',
                         	-- or       , branch = '0.1.x',
		requires = 'nvim-lua/plenary.nvim'
  }
  --Панель вкладок
  use {'akinsho/bufferline.nvim', tag = "v3.*",
    requires = 'nvim-tree/nvim-web-devicons'
  }
  -- Статуслайн
	use {'nvim-lualine/lualine.nvim',
		requires = { 'kyazdani42/nvim-web-devicons', opt = true },
		config = function()
			require('plugins/lualine') end
  }
	-- LSP сервер
	use 'williamboman/mason.nvim' -- Инсталлер для серверов LSP
	use 'williamboman/mason-lspconfig.nvim'
	use 'neovim/nvim-lspconfig'
  -- Автодополнение
	use {'hrsh7th/nvim-cmp',
		requires = {
			'L3MON4D3/LuaSnip',
			'saadparwaiz1/cmp_luasnip',
			'hrsh7th/cmp-nvim-lsp',
			'hrsh7th/cmp-path',
			'hrsh7th/cmp-emoji',
			'hrsh7th/cmp-nvim-lsp-signature-help',
			'hrsh7th/cmp-nvim-lua'
  	},
		config = function()
		-- ДАННАЯ ЧАСТЬ ОЧЕНЬ ВАЖНА:
			require('plugins/cmp') end
  }

  -- use 'nvim-lua/plenary.nvim'
	
	--Темы уточнить
	use 'terroo/vim-simple-emoji'
	use 'navarasu/onedark.nvim'
	use 'gruvbox-community/gruvbox'


end)


	-- Simple plugins can be specified as strings
    --[[--
    use 'rstacruz/vim-closer'
    --]]--

    -- Lazy loading:
    -- Load on specific commands
    --[[--
    use {'tpope/vim-dispatch', opt = true, cmd = {'Dispatch', 'Make', 'Focus', 'Start'}}
    --]]--

    -- Load on an autocommand event
    --[[--
    use {'andymass/vim-matchup', event = 'VimEnter'}
    --]]--

    -- Load on a combination of conditions: specific filetypes or commands
    -- Also run code after load (see the "config" key)
    --use {
        --'w0rp/ale',
            --ft = {'sh', 'zsh', 'bash', 'c', 'cpp', 'cmake', 'html', 'markdown', 'racket', 'vim', 'tex'},
            --cmd = 'ALEEnable',
            --config = 'vim.cmd[[ALEEnable]]'}

    -- Plugins can have dependencies on other plugins
    --[[--
    use {'haorenW1025/completion-nvim',opt = true,
    requires = {{'hrsh7th/vim-vsnip', opt = true}, {'hrsh7th/vim-vsnip-integ', opt = true}}}
    --]]--

    -- Plugins can have post-install/update hooks
    --[[--
    use {'iamcco/markdown-preview.nvim', run = 'cd app && yarn install', cmd = 'MarkdownPreview'}
    --]]--

    -- Post-install/update hook with neovim command
    --[[--
    use { 'nvim-treesitter/nvim-treesitter', run = ':TSUpdate' }
    --]]--

    -- Post-install/update hook with call of vimscript function with argument
    --[[--
    use { 'glacambre/firenvim', run = function() vim.fn['firenvim#install'](0) end }
    --]]--

    -- Use dependency and run lua function after load
    --[[--
    use {
        'lewis6991/gitsigns.nvim',
          requires = { 'nvim-lua/plenary.nvim' },
          config = function() require('gitsigns').setup() end
    }
    --]]--

    -- You can specify multiple plugins in a single call
    --[[--
    use {'tjdevries/colorbuddy.vim', {'nvim-treesitter/nvim-treesitter', opt = true}}
    --]]--

    -- You can alias plugin names
    --[[--
    use { 'dracula/vim', as = 'dracula' }
    --]]--











