This repository contains sources for RPMs that are used
to build Software Collections for CentOS by SCLo SIG.

This branch is for sclo-php72 packages (for rh-php72 SCL)


PHP 7.2 / EL 7

    build -bs *spec --define "scl rh-php72" --define "dist .el7"
    cbs add-pkg    sclo7-sclo-php72-sclo-candidate --owner=sclo  sclo-php72-php-tidy
    cbs add-pkg    sclo7-sclo-php72-sclo-testing   --owner=sclo  sclo-php72-php-tidy
    cbs add-pkg    sclo7-sclo-php72-sclo-release   --owner=sclo  sclo-php72-php-tidy
    cbs build      sclo7-sclo-php72-sclo-el7       <above>.src.rpm
    cbs tag-build  sclo7-sclo-php72-sclo-testing   <previous>

