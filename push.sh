jupyter-book build .

echo '===================='

git add ./*
git commit -m "$1"
git push
