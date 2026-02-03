#!/bin/bash
#
# repair_latest_alias.sh
# One-time repair script to fix /latest/ alias to point to the correct release version
#
# This script should be run when /latest/ has diverged from the most recent release.
# It deletes the current /latest/ and recreates it as a proper redirect alias.
#
# Usage:
#   ./tooling/release/repair_latest_alias.sh [VERSION]
#
# If VERSION is not provided, it will use the most recent version found in gh-pages.
#
# Prerequisites:
#   - Git repository with gh-pages branch
#   - mike installed (pip install mike)
#   - Write access to gh-pages branch
#
# Safety:
#   - This script does NOT modify versioned directories (e.g., /0.1.x/)
#   - It only affects the /latest/ alias
#

set -euo pipefail

# Color output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo ""
echo "======================================================================"
echo "  AIMO Standard - Repair /latest/ Alias"
echo "======================================================================"
echo ""

# Get version from argument or detect from gh-pages
if [ -n "${1:-}" ]; then
    VERSION="$1"
    echo "Using specified version: $VERSION"
else
    echo "No version specified, detecting most recent release..."
    
    # Fetch gh-pages
    git fetch origin gh-pages:gh-pages 2>/dev/null || {
        echo -e "${RED}ERROR: Could not fetch gh-pages branch${NC}"
        exit 1
    }
    
    # Find version directories (X.Y.Z format)
    VERSIONS=$(git ls-tree --name-only gh-pages | grep -E '^[0-9]+\.[0-9]+\.[0-9]+$' | sort -V)
    
    if [ -z "$VERSIONS" ]; then
        echo -e "${RED}ERROR: No version directories found in gh-pages${NC}"
        exit 1
    fi
    
    # Get the latest version
    VERSION=$(echo "$VERSIONS" | tail -1)
    echo "Detected most recent version: $VERSION"
fi

echo ""
echo "This script will:"
echo "  1. Delete the current /latest/ alias (if it exists)"
echo "  2. Recreate /latest/ as a redirect alias to /$VERSION/"
echo "  3. Set /latest/ as the default version"
echo ""
echo -e "${YELLOW}WARNING: This will modify the gh-pages branch.${NC}"
echo ""
read -p "Continue? (y/N) " -n 1 -r
echo ""

if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Aborted."
    exit 0
fi

echo ""
echo "=== Step 1: Verify version $VERSION exists ==="

git fetch origin gh-pages:gh-pages || true

if ! git ls-tree --name-only gh-pages | grep -q "^${VERSION}$"; then
    echo -e "${RED}ERROR: Version $VERSION does not exist in gh-pages${NC}"
    echo "Available versions:"
    git ls-tree --name-only gh-pages | grep -E '^[0-9]+\.[0-9]+\.[0-9]+$' | sort -V
    exit 1
fi

echo -e "${GREEN}✓ Version $VERSION exists${NC}"

echo ""
echo "=== Step 2: Current mike state ==="
mike list || echo "(No versions configured yet)"

echo ""
echo "=== Step 3: Delete existing /latest/ alias ==="

# Delete latest if it exists (this only removes the alias, not the version)
mike delete latest --push 2>/dev/null && echo -e "${GREEN}✓ Deleted existing /latest/${NC}" || echo "No existing /latest/ to delete"

echo ""
echo "=== Step 4: Recreate /latest/ as redirect to /$VERSION/ ==="

# Deploy with update-aliases to create the redirect
mike deploy --push --update-aliases "$VERSION" latest

echo -e "${GREEN}✓ Created /latest/ -> /$VERSION/${NC}"

echo ""
echo "=== Step 5: Set /latest/ as default ==="

mike set-default --push latest

echo -e "${GREEN}✓ Set /latest/ as default${NC}"

echo ""
echo "=== Step 6: Verification ==="

echo "Current mike versions:"
mike list

# Verify the alias
ALIAS_INFO=$(mike list | grep "$VERSION")
if echo "$ALIAS_INFO" | grep -q "latest"; then
    echo ""
    echo -e "${GREEN}======================================================================"
    echo "  SUCCESS: /latest/ now redirects to /$VERSION/"
    echo "======================================================================${NC}"
else
    echo ""
    echo -e "${RED}ERROR: Verification failed - latest may not be correctly set${NC}"
    exit 1
fi

echo ""
echo "To verify on the live site:"
echo "  curl -sI https://standard.aimoaas.com/latest/ | grep -i location"
echo ""
echo "Expected: Redirect to /${VERSION}/"
echo ""
