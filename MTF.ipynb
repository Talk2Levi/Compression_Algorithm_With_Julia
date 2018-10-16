using Test

num = collect('0':'9')
letter = collect('A':'z')
pun = [' ','.',',','?','!','/', '-', '_', '\n','\t', ':', ';', '"', '\'' ]

function encodeMTF(str::AbstractString, symtable::Vector{Char}=vcat(letter,pun,num))
    function encode(ch::Char)
        r = findfirst(x->x==ch, symtable)
        deleteat!(symtable, r)
        prepend!(symtable, ch)
        r
    end
    [encode(ch) for ch in str]
end
 
function decodeMTF(arr::Vector{Int}, symtable::Vector{Char}=vcat(letter,pun,num))
    function decode(i::Int)
        r = symtable[i]
        deleteat!(symtable, i)
        prepend!(symtable, r)
        r
    end
    join(decode(i) for i in arr)
end
 
function originalAccess(str::AbstractString, symtable::Vector{Char}=vcat(letter,pun,num))
    function originalIndividualCost(ch::Char)
        r = findfirst(x->x==ch, symtable)
    end
    [originalIndividualCost(ch) for ch in str]
end


"""
Running
"""
testSequence = ["Man is the only creature that consumes without producing. He does not give milk, he does not lay eggs, he is too weak to pull the plough, he cannot run fast enough to catch rabbits. Yet he is lord of all the animals. He sets them to work, he gives back to them the bare minimum that will prevent them from starving, and the rest he keeps for himself."]
encodedSequence = encodeMTF.(testSequence)
decodedSequence = decodeMTF.(encodedSequence)
originalSequence = originalAccess.(testSequence)

encodedCost = sum(encodedSequence[1])
originalCost = sum(originalSequence[1])

println("Functionality Check")
for (test, dec) in zip(testSequence, decodedSequence)
    println("-> Test string: \n$test\n-> Decoded seq: \n$dec\n")
end

savedCostPerc = (round(1 - encodedCost/originalCost, sigdigits=5))*100
println("Look Up Cost")
println("Total Cost Using MTF Algorithm: $encodedCost")
println("Total Cost Using Original Access: $originalCost")
println("Total Look up cost saved $savedCostPerc%\n")


"""
Unit test for compression algorithm
"""
@testset "Successfully Decoded Test" begin
    for (seq, dec) in zip(testSequence, decodedSequence)
        @test seq == dec
    end
end
