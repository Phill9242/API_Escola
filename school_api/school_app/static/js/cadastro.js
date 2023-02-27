// MODAL CADASTRO ALUNO -----------------------------------------------------------------------
const abrirModalAluno = document.querySelector("#abrir-modal-aluno");
const fecharModalAluno = document.querySelector("#fechar-modal-aluno");
const modalAluno = document.querySelector("#modal-aluno");
const fadeAluno = document.querySelector("#fade-aluno");


[abrirModalAluno, fecharModalAluno, fadeAluno, ].forEach((element)=>{
    element.addEventListener ("click", () => modificarModalAluno());
})

const   modificarModalAluno = () => {
    modalAluno.classList.toggle("hide");
    fadeAluno.classList.toggle("hide");
}

// MODAL CADASTRO PROFESSOR -----------------------------------------------------------------------

const fadeProfessor = document.querySelector("#fade-professor");
const abrirModalProfessor = document.querySelector("#abrir-modal-professor");
const fecharModalProfessor = document.querySelector("#fechar-modal-professor");
const modalProfessor = document.querySelector("#modal-professor");
[abrirModalProfessor, fecharModalProfessor, fadeProfessor, ].forEach((element)=>{
    element.addEventListener ("click", () => modificarModalProfessor());
})

const   modificarModalProfessor = () => {
    modalProfessor.classList.toggle("hide");
    fadeProfessor.classList.toggle("hide");
}

// MODAL CADASTRO CURSO -----------------------------------------------------------------------

const fadeCurso = document.querySelector("#fade-curso");
const abrirModalCurso = document.querySelector("#abrir-modal-curso");
const fecharModalCurso = document.querySelector("#fechar-modal-curso");
const modalCurso = document.querySelector("#modal-curso");

[abrirModalCurso, fecharModalCurso, fadeCurso, ].forEach((element)=>{
    element.addEventListener ("click", () => modificarModalCurso());
})

const   modificarModalCurso = () => {
    modalCurso.classList.toggle("hide");
    fadeCurso.classList.toggle("hide");
}
