This repository contains sources for RPMs that are used
to build Software Collections for CentOS by SCLo SIG.

This branch is for sclo-php71 packages (for rh-php71 SCL)


PHP 7.1 / EL 7

    build -bs *spec --define "scl rh-php71" --define "dist .el7"
    cbs add-pkg    sclo7-sclo-php71-sclo-candidate --owner=sclo  sclo-php71-php-tidy
    cbs add-pkg    sclo7-sclo-php71-sclo-testing   --owner=sclo  sclo-php71-php-tidy
    cbs add-pkg    sclo7-sclo-php71-sclo-release   --owner=sclo  sclo-php71-php-tidy
    cbs build      sclo7-sclo-php71-sclo-el7       <above>.src.rpm
    cbs tag-build  sclo7-sclo-php71-sclo-testing   <previous>

