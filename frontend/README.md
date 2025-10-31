# Roots & Recipes Frontend

Modern, responsive React frontend for the Roots & Recipes application.

## 🚀 Quick Start

### Prerequisites
- Node.js 18+ and npm/yarn
- Backend API running on `http://localhost:8000`

### Installation

1. **Install dependencies**:
   ```bash
   npm install
   # or
   yarn install
   ```

2. **Set up environment variables**:
   Create a `.env` file in the frontend directory (copy from `.env.example`):
   ```env
   VITE_API_BASE_URL=http://localhost:8000
   ```

3. **Run the development server**:
   ```bash
   npm run dev
   # or
   yarn dev
   ```

   The app will be available at: `http://localhost:5173`

## 📁 Project Structure

```
frontend/
├── src/
│   ├── components/          # Reusable UI components
│   │   ├── Navbar.tsx      # Navigation bar with theme/language toggles
│   │   ├── Footer.tsx      # Footer component
│   │   ├── Loading.tsx     # Loading spinner
│   │   └── ErrorMessage.tsx # Error display
│   ├── pages/              # Page components
│   │   ├── HomePage.tsx    # Home page with featured dishes
│   │   ├── DishDetailPage.tsx   # Individual dish view
│   │   ├── IngredientDetailPage.tsx # Ingredient details
│   │   └── NotFoundPage.tsx     # 404 page
│   ├── services/           # API clients
│   │   └── api.ts          # Axios-based API client
│   ├── hooks/              # Custom React hooks
│   │   └── index.ts        # useTheme, useWindowSize, etc.
│   ├── i18n/               # Internationalization
│   │   ├── index.ts        # i18n configuration
│   │   └── locales/        # Translation files (EN, DE)
│   ├── types/              # TypeScript definitions
│   │   └── index.ts        # Type definitions
│   ├── utils/              # Utility functions
│   │   └── helpers.ts      # Helper functions
│   ├── App.tsx             # Main app component with routing
│   ├── main.tsx            # Entry point
│   └── index.css           # Global styles with Tailwind
├── public/                 # Static assets
├── index.html              # HTML template
├── package.json            # Dependencies
├── tsconfig.json           # TypeScript config
├── tailwind.config.js      # Tailwind CSS config
├── vite.config.ts          # Vite configuration
└── README.md               # This file
```

## 🎨 Features

### Implemented
- ✅ **Responsive Design**: Mobile-first design with Tailwind CSS
- ✅ **Dark Mode**: Toggle between light and dark themes
- ✅ **Internationalization**: English and German translations
- ✅ **Type Safety**: Full TypeScript support
- ✅ **Modern UI**: Clean, accessible components with Lucide icons
- ✅ **API Integration**: Axios-based API client with type safety
- ✅ **Routing**: React Router v6 for navigation
- ✅ **Loading States**: Proper loading and error handling

### TODO (Enhancements)
- 🔜 **MapLibre Integration**: Interactive map on home page
- 🔜 **Image Gallery**: Lightbox for dish images
- 🔜 **Video Player**: Embedded video support
- 🔜 **Ingredient Modal**: Interactive ingredient chips
- 🔜 **Filters**: Advanced filtering on home page
- 🔜 **Search**: Full-text search functionality
- 🔜 **Dinner Mode**: QR code generation
- 🔜 **PWA**: Service worker for offline support
- 🔜 **Animations**: Framer Motion for page transitions

## 🛠 Tech Stack

- **React 18** - UI library
- **TypeScript** - Type safety
- **Vite** - Build tool and dev server
- **Tailwind CSS** - Utility-first CSS framework
- **React Router v6** - Client-side routing
- **Axios** - HTTP client
- **react-i18next** - Internationalization
- **Lucide React** - Icon library

## 🎯 Available Scripts

```bash
# Development
npm run dev          # Start dev server (http://localhost:5173)

# Building
npm run build        # Build for production
npm run preview      # Preview production build

# Linting
npm run lint         # Run ESLint
```

## 🌐 Environment Variables

Create a `.env` file in the frontend directory:

```env
# API Base URL
VITE_API_BASE_URL=http://localhost:8000
```

## 🎨 Customization

### Theme Colors
Edit `tailwind.config.js` to customize the color scheme:

```javascript
theme: {
  extend: {
    colors: {
      primary: {
        // Your custom colors
      },
    },
  },
}
```

### Translations
Add or edit translations in `src/i18n/locales/`:
- `en.json` - English
- `de.json` - German
- Add `bn.json` for Bangla support

## 📱 Responsive Breakpoints

```css
sm: 640px   /* Small devices */
md: 768px   /* Tablets */
lg: 1024px  /* Desktops */
xl: 1280px  /* Large desktops */
2xl: 1536px /* Extra large */
```

## 🔧 Development Tips

### Hot Module Replacement
Vite provides instant HMR. Changes are reflected immediately without full page reload.

### TypeScript Errors
The import errors you see before `npm install` are normal. They'll disappear once dependencies are installed.

### Dark Mode Testing
Toggle dark mode using the moon/sun icon in the navigation bar. Preferences are saved to localStorage.

### Language Switching
Use the globe icon to switch between English and German.

## 🚢 Production Build

```bash
# Build for production
npm run build

# The output will be in the `dist/` directory
# Serve it with any static file server
npm run preview
```

## 📦 Deployment

The built files in `dist/` can be deployed to:
- **Vercel**: `vercel --prod`
- **Netlify**: Drag & drop `dist/` folder
- **GitHub Pages**: Use GitHub Actions
- **AWS S3**: Upload to S3 bucket
- **Any static hosting**: Serve the `dist/` directory

### Environment Variables for Production
Make sure to set `VITE_API_BASE_URL` to your production API URL.

## 🧪 Testing (TODO)

```bash
# Unit tests
npm test

# E2E tests
npm run test:e2e
```

## 📄 License

MIT License - See main project README for details.

## 🤝 Contributing

1. Follow the existing code style
2. Use TypeScript for all new components
3. Add translations for new text
4. Test in both light and dark modes
5. Ensure mobile responsiveness

---

**Happy coding! 🎉**
